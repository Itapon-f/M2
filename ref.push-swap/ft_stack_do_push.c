/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_stack_do_push.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: agiron-d <agiron-d@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/27 12:48:26 by agiron-d          #+#    #+#             */
/*   Updated: 2025/12/01 05:17:49 by agiron-d         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ft_pa(t_stack **a, t_stack **b, int w)
{
	t_stack	*node;

	if (!b || !*b)
		return ;
	node = ft_stack_remove_first(b);
	ft_stack_add_front(a, node);
	if (w)
		ft_putstr("pa\n");
}

void	ft_pb(t_stack **a, t_stack **b, int w)
{
	t_stack	*node;

	if (!a || !*a)
		return ;
	node = ft_stack_remove_first(a);
	ft_stack_add_front(b, node);
	if (w)
		ft_putstr("pb\n");
}
