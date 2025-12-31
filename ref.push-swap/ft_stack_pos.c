/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_stack_pos.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: agiron-d <agiron-d@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/27 17:38:27 by agiron-d          #+#    #+#             */
/*   Updated: 2025/11/28 08:14:41 by agiron-d         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static int	ft_find_pos_helper(t_stack *stack_b,
		t_stack	*target, t_stack *current, int pos)
{
	int		size;
	int		i;

	if (!target)
	{
		size = ft_stack_size(stack_b);
		current = stack_b;
		target = current;
		pos = 0;
		i = 0;
		while (i < size)
		{
			if (current->nbr < target->nbr)
			{
				target = current;
				pos = i;
			}
			current = current->next;
			i++;
		}
	}
	return (pos);
}

int	ft_find_target_pos(t_stack *stack_b, long value)
{
	t_stack	*current;
	t_stack	*target;
	int		pos;
	int		i;

	if (!stack_b)
		return (0);
	current = stack_b;
	target = NULL;
	pos = 0;
	i = -1;
	while (++i < ft_stack_size(stack_b))
	{
		if (current->nbr > value && (!target || current->nbr < target->nbr))
		{
			target = current;
			pos = i;
		}
		current = current->next;
	}
	return (ft_find_pos_helper(stack_b, target, current, pos));
}

int	ft_get_position(t_stack *stack, t_stack *node)
{
	t_stack	*current;
	int		pos;

	if (!stack || !node)
		return (-1);
	current = stack;
	pos = 0;
	while (current != node)
	{
		current = current->next;
		pos++;
		if (current == stack)
			return (-1);
	}
	return (pos);
}
