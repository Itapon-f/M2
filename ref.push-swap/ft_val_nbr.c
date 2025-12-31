/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_val_nbr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: agiron-d <agiron-d@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/27 13:47:38 by agiron-d          #+#    #+#             */
/*   Updated: 2025/12/02 03:22:27 by agiron-d         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

long	ft_find_min(t_stack *stack)
{
	long	min;
	t_stack	*current;
	int		size;
	int		i;

	if (!stack)
		return (0);
	min = stack->nbr;
	current = stack;
	size = ft_stack_size(stack);
	i = 0;
	while (i < size)
	{
		if (current->nbr < min)
			min = current->nbr;
		current = current->next;
		i++;
	}
	return (min);
}

long	ft_find_max(t_stack *stack)
{
	long	max;
	t_stack	*current;
	int		size;
	int		i;

	if (!stack)
		return (0);
	max = stack->nbr;
	current = stack;
	size = ft_stack_size(stack);
	i = 0;
	while (i < size)
	{
		if (current->nbr > max)
			max = current->nbr;
		current = current->next;
		i++;
	}
	return (max);
}

int	ft_validate_number(const char *str)
{
	int	i;

	i = 0;
	while (ft_is_space(str[i]))
		i++;
	if (str[i] == '-' || str[i] == '+')
		i++;
	if (!str[i] || !(str[i] >= '0' && str[i] <= '9'))
		return (0);
	while (str[i] && (str[i] >= '0' && str[i] <= '9'))
		i++;
	while (ft_is_space(str[i]))
		i++;
	return (str[i] == 0);
}
